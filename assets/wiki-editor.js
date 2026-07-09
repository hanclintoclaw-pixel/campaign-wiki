(() => {
  const ISSUE_URL_MAX_LENGTH = 7000
  const APP_ID = 'campaign-wiki-editor'
  const APP_NAME = 'Campaign Wiki Editor'

  function meta(name, fallback = '') {
    return document.querySelector(`meta[name="${name}"]`)?.getAttribute('content') || fallback
  }

  const repository = meta('campaign-wiki-repository', 'hanclintoclaw-pixel/campaign-wiki')
  const sourceCommit = meta('campaign-wiki-source-commit', 'master')
  const sourceBranch = meta('campaign-wiki-source-branch', 'master')
  const sourceRef = sourceCommit && sourceCommit !== 'local-dev' ? sourceCommit : sourceBranch

  function pagePathFromLocation() {
    const siteBase = document.querySelector('script[src$="/assets/wiki-editor.js"]')?.getAttribute('src')?.replace(/assets\/wiki-editor\.js(?:\?.*)?$/, '') || '/'
    const basePath = new URL(siteBase, window.location.origin).pathname.replace(/\/$/, '')
    let path = decodeURIComponent(window.location.pathname)
    if (basePath && path.startsWith(basePath)) {
      path = path.slice(basePath.length)
    }
    path = path.replace(/^\//, '')

    if (!path) return 'index.md'
    if (path.endsWith('/')) return `${path}README.md`
    if (path.endsWith('.html')) return `${path.slice(0, -5)}.md`
    if (path.endsWith('.md')) return path
    return `${path}/README.md`
  }

  function rawUrlFor(path) {
    const encodedPath = path.split('/').map(encodeURIComponent).join('/')
    return `https://raw.githubusercontent.com/${repository}/${encodeURIComponent(sourceRef)}/${encodedPath}`
  }

  function issueUrlFor(title, body) {
    const params = new URLSearchParams({
      title,
      labels: 'wiki-edit,needs-review',
      body,
    })
    return `https://github.com/${repository}/issues/new?${params.toString()}`
  }

  function bodyFor(request) {
    return `## Human summary\n\n${request.summary}\n\n## Machine-readable request\n\n\`\`\`json\n${JSON.stringify(request, null, 2)}\n\`\`\`\n`
  }

  function attachmentBodyFor(request, filename) {
    return `## Human summary\n\n${request.summary}\n\n## Machine-readable request\n\nThe Markdown patch request was too large for a prefilled GitHub Issue URL. Please attach the downloaded file to this issue before submitting it.\n\nExpected attachment: \`${filename}\`\n`
  }

  function splitLines(text) {
    return text.replace(/\r\n/g, '\n').replace(/\r/g, '\n').split('\n')
  }

  function buildLinePatch(beforeText, afterText) {
    const before = splitLines(beforeText)
    const after = splitLines(afterText)
    const rows = Array.from({ length: before.length + 1 }, () => new Uint32Array(after.length + 1))

    for (let i = before.length - 1; i >= 0; i -= 1) {
      for (let j = after.length - 1; j >= 0; j -= 1) {
        rows[i][j] = before[i] === after[j] ? rows[i + 1][j + 1] + 1 : Math.max(rows[i + 1][j], rows[i][j + 1])
      }
    }

    const hunks = []
    let hunk = null
    let i = 0
    let j = 0
    let originalLine = 1

    function ensureHunk() {
      if (!hunk) {
        hunk = { startLine: originalLine, deleteCount: 0, insertLines: [] }
      }
      return hunk
    }

    function flushHunk() {
      if (hunk) {
        hunks.push(hunk)
        hunk = null
      }
    }

    while (i < before.length || j < after.length) {
      if (i < before.length && j < after.length && before[i] === after[j]) {
        flushHunk()
        i += 1
        j += 1
        originalLine += 1
      } else if (i < before.length && (j >= after.length || rows[i + 1][j] >= rows[i][j + 1])) {
        ensureHunk().deleteCount += 1
        i += 1
        originalLine += 1
      } else {
        ensureHunk().insertLines.push(after[j])
        j += 1
      }
    }

    flushHunk()
    return {
      hunks,
      originalLineCount: before.length,
      resultingLineCount: after.length,
      changedLineCount: hunks.reduce((total, item) => total + item.deleteCount + item.insertLines.length, 0),
    }
  }

  async function sha256(text) {
    const bytes = new TextEncoder().encode(text)
    const digest = await crypto.subtle.digest('SHA-256', bytes)
    return Array.from(new Uint8Array(digest), (byte) => byte.toString(16).padStart(2, '0')).join('')
  }

  function downloadTextFile(filename, content) {
    const blob = new Blob([content], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = filename
    link.click()
    URL.revokeObjectURL(url)
  }

  function requestDraft(request) {
    const title = `Edit wiki page: ${request.pagePath}`
    const prefilledUrl = issueUrlFor(title, bodyFor(request))
    if (prefilledUrl.length <= ISSUE_URL_MAX_LENGTH) {
      return { url: prefilledUrl }
    }

    const safeName = request.pagePath.replace(/[^a-z0-9]+/gi, '-').replace(/^-|-$/g, '').toLowerCase() || 'wiki-page'
    const filename = `${safeName}-wiki-edit-request-${new Date().toISOString().slice(0, 10)}.json`
    return {
      url: issueUrlFor(title, attachmentBodyFor(request, filename)),
      attachment: {
        filename,
        content: `${JSON.stringify(request, null, 2)}\n`,
      },
    }
  }

  function createShell(pagePath) {
    const shell = document.createElement('section')
    shell.className = 'wiki-editor-shell'
    shell.innerHTML = `
      <div class="wiki-editor-toolbar">
        <div>
          <strong>Wiki editor</strong>
          <div class="wiki-editor-status" data-wiki-editor-status>Raw Markdown: ${pagePath}</div>
        </div>
        <div class="wiki-editor-actions">
          <button class="wiki-editor-button" type="button" data-wiki-editor-edit>Edit</button>
          <button class="wiki-editor-button" type="button" data-wiki-editor-cancel disabled>Cancel</button>
          <button class="wiki-editor-button primary" type="button" data-wiki-editor-save disabled>Save changes</button>
        </div>
      </div>
      <div class="wiki-editor-form wiki-editor-hidden" data-wiki-editor-form>
        <label class="wiki-editor-label">Change summary
          <input class="wiki-editor-input" type="text" data-wiki-editor-summary placeholder="What changed and why?">
        </label>
        <textarea class="wiki-editor-textarea" spellcheck="true" data-wiki-editor-textarea></textarea>
        <p class="wiki-editor-help">Save changes opens a GitHub Issue containing a Markdown line patch, source commit, source hash, and target path. It does not write directly to the wiki.</p>
      </div>
    `
    return shell
  }

  function mountEditor() {
    const pagePath = pagePathFromLocation()
    if (pagePath.startsWith('assets/')) return

    const content = document.querySelector('main .wrapper') || document.querySelector('.page-content .wrapper') || document.querySelector('main') || document.body
    const shell = createShell(pagePath)
    content.prepend(shell)

    const editButton = shell.querySelector('[data-wiki-editor-edit]')
    const cancelButton = shell.querySelector('[data-wiki-editor-cancel]')
    const saveButton = shell.querySelector('[data-wiki-editor-save]')
    const form = shell.querySelector('[data-wiki-editor-form]')
    const status = shell.querySelector('[data-wiki-editor-status]')
    const textarea = shell.querySelector('[data-wiki-editor-textarea]')
    const summaryInput = shell.querySelector('[data-wiki-editor-summary]')

    let originalText = ''
    let originalHash = ''
    let loaded = false

    function hasChanges() {
      return loaded && textarea.value !== originalText
    }

    function refreshButtons() {
      cancelButton.disabled = !loaded
      saveButton.disabled = !hasChanges()
      status.textContent = hasChanges()
        ? `Editing ${pagePath} - unsaved issue request changes`
        : loaded
          ? `Editing ${pagePath} - no local changes`
          : `Raw Markdown: ${pagePath}`
    }

    async function enterEditMode() {
      form.classList.remove('wiki-editor-hidden')
      editButton.disabled = true
      status.textContent = `Loading ${pagePath}...`

      if (!loaded) {
        const response = await fetch(rawUrlFor(pagePath), { cache: 'no-store' })
        if (!response.ok) {
          throw new Error(`Could not load raw Markdown (${response.status} ${response.statusText}).`)
        }
        originalText = await response.text()
        originalHash = await sha256(originalText)
        textarea.value = originalText
        summaryInput.value = `Update ${pagePath}`
        loaded = true
      }

      refreshButtons()
    }

    editButton.addEventListener('click', () => {
      enterEditMode().catch((error) => {
        status.textContent = error instanceof Error ? error.message : 'Could not load editor.'
        editButton.disabled = false
      })
    })

    cancelButton.addEventListener('click', () => {
      textarea.value = originalText
      form.classList.add('wiki-editor-hidden')
      editButton.disabled = false
      refreshButtons()
    })

    textarea.addEventListener('input', refreshButtons)

    saveButton.addEventListener('click', async () => {
      if (!hasChanges()) return

      const patch = buildLinePatch(originalText, textarea.value)
      const summary = summaryInput.value.trim() || `Update ${pagePath}`
      const request = {
        schemaVersion: 'campaign-wiki-edit/v1',
        appId: APP_ID,
        appName: APP_NAME,
        createdAt: new Date().toISOString(),
        sourceRepository: repository,
        sourceCommit,
        sourceRef,
        pagePath,
        originalSha256: originalHash,
        summary,
        requestedChanges: [
          {
            type: 'patch_markdown_file',
            targetPath: pagePath,
            baseSnapshot: `${sourceCommit}:${pagePath}`,
            baseSha256: originalHash,
            format: 'line-patch/v1',
            payload: patch,
          },
        ],
      }
      const draft = requestDraft(request)
      if (draft.attachment) {
        downloadTextFile(draft.attachment.filename, draft.attachment.content)
        status.textContent = `Downloaded ${draft.attachment.filename}; attach it to the GitHub Issue before submitting.`
      } else {
        status.textContent = 'Opened a GitHub Issue with the Markdown patch request prefilled.'
      }
      window.open(draft.url, '_blank', 'noopener,noreferrer')
    })
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mountEditor)
  } else {
    mountEditor()
  }
})()
