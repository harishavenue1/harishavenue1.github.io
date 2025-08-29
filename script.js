// Function to fetch and inject code snippets based on program selection
function selectProgram(program) {
    const languageCards = document.querySelectorAll('.code-container');
    let fileExtn = ''
    languageCards.forEach(card => {
        const language = card.dataset.language;
        const targetId = language + "-code";
        card.style.display = "block";
        if (language == 'csharp')
            fileExtn = 'cs'
        else if (language == 'java')
            fileExtn = 'java'
        else if (language == 'python')
            fileExtn = 'py'
        else
            fileExtn = 'js'

        const baseUrl = window.location.hostname === 'localhost' ? 
            './programs/' : 
            'https://raw.githubusercontent.com/harishavenue1/harishavenue1.github.io/main/programs/';
        fetchCode(baseUrl + program + '/' + language + '_code.' + fileExtn, targetId);
    });

    updatePageTitle(program.charAt(0).toUpperCase() + program.slice(1));
}

// Function to fetch and inject code snippets
function fetchCode(url, targetId) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('File not found');
            }
            return response.text();
        })
        .then(data => {
            document.getElementById(targetId).textContent = data;
            document.getElementById(targetId).parentElement.scrollTop = 0;
            Prism.highlightAll();
        })
        .catch(error => {
            document.getElementById(targetId).textContent = 'Code not available for this language';
        });
}

// Function to update page title and h1 based on selected program
function updatePageTitle(program) {
    document.title = "Code Comparison - " + program;
    document.getElementById('comparison-title').textContent = "Code Comparison - " + program;
}

// Function to toggle maximize
function toggleMaximize(button) {
    const container = button.closest('.code-container');
    const title = container.querySelector('.code-title').textContent.replace(' 📋', '').replace(' ⛶', '').replace(' ✕', '').trim();
    const codeContent = container.querySelector('code').textContent;
    
    // Create fullscreen modal
    const modal = document.createElement('div');
    modal.className = 'fullscreen-modal';
    modal.style.display = 'block';
    
    modal.innerHTML = `
        <div class="fullscreen-content">
            <div class="code-title">${title} 
                <button class="copy-btn" onclick="copyCodeFromModal(this)">📋</button>
                <button class="maximize-btn" onclick="closeMaximize(this)">✕</button>
            </div>
            <pre><code class="language-${title.toLowerCase()}">${codeContent}</code></pre>
        </div>
    `;
    
    document.body.appendChild(modal);
    Prism.highlightAll();
}

// Function to close maximize
function closeMaximize(button) {
    const modal = button.closest('.fullscreen-modal');
    document.body.removeChild(modal);
}

// Function to copy code to clipboard
function copyCode(button) {
    const container = button.closest('.code-container');
    const codeContent = container.querySelector('code').textContent;
    
    navigator.clipboard.writeText(codeContent).then(() => {
        // Show feedback
        const originalText = button.innerHTML;
        button.innerHTML = '✓';
        button.style.background = 'rgba(34, 197, 94, 0.3)';
        
        setTimeout(() => {
            button.innerHTML = originalText;
            button.style.background = '#D5CBFD';
        }, 1000);
    }).catch(() => {
        alert('Failed to copy code');
    });
}

// Function to copy code from fullscreen modal
function copyCodeFromModal(button) {
    const modal = button.closest('.fullscreen-modal');
    const codeContent = modal.querySelector('code').textContent;
    
    navigator.clipboard.writeText(codeContent).then(() => {
        // Show feedback
        const originalText = button.innerHTML;
        button.innerHTML = '✓';
        button.style.background = 'rgba(34, 197, 94, 0.3)';
        
        setTimeout(() => {
            button.innerHTML = originalText;
            button.style.background = '#D5CBFD';
        }, 1000);
    }).catch(() => {
        alert('Failed to copy code');
    });
}

// Initially select the first program
selectProgram('fibonacci');
