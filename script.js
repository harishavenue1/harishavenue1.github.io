// Function to fetch and inject code snippets based on program selection
function selectProgram(program) {
    const languageCards = document.querySelectorAll('.code-container');
    let fileExtn = ''
    languageCards.forEach(card => {
        const language = card.querySelector('.code-title').textContent.toLowerCase();
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

        fetchCode('./programs/' + program + '/' + language + '_code.' + fileExtn, targetId);
    });

    updatePageTitle(program.charAt(0).toUpperCase() + program.slice(1));
}

// Function to fetch and inject code snippets
function fetchCode(url, targetId) {
    fetch(url)
        .then(response => response.text())
        .then(data => {
            document.getElementById(targetId).textContent = data;
        })
        .catch(error => console.error('Error fetching code:', error));
}

// Function to update page title and h1 based on selected program
function updatePageTitle(program) {
    document.title = "Code Comparison - " + program;
    document.getElementById('comparison-title').textContent = "Code Comparison - " + program;
}

// Initially select the first program
selectProgram('fibonacci');
