const questions = [
    { text: "Do you prefer warm or cold climates?", options: { "Warm": "warm", "Cold": "cold" } },
    { text: "Do you like historical places or modern cities?", options: { "Historical": "historical", "Modern": "modern" } },
    { text: "Are you interested in nature or urban life?", options: { "Nature": "nature", "Urban": "urban" } },
    { text: "Do you prefer a budget-friendly or luxury trip?", options: { "Budget-friendly": "budget", "Luxury": "luxury" } },
    { text: "What kind of food do you like?", options: { "Local": "local", "International": "international" } }
];

// Ülkeleri belirleyen veri yapısı
const countryPreferences = {
    "Germany": ["cold", "modern", "urban", "budget", "international"],
    "Austria": ["cold", "historical", "nature", "luxury", "local"],
    "Belgium": ["cold", "modern", "urban", "budget", "international"],
    "Bulgaria": ["warm", "historical", "nature", "budget", "local"],
    "Czechia": ["cold", "historical", "urban", "budget", "local"],
    "Denmark": ["cold", "modern", "urban", "luxury", "international"],
    "Estonia": ["cold", "historical", "nature", "budget", "local"],
    "Finland": ["cold", "nature", "budget", "local"],
    "France": ["warm", "historical", "urban", "luxury", "international"],
    "Cyprus": ["warm", "historical", "nature", "luxury", "local"],
    "Croatia": ["warm", "historical", "nature", "budget", "local"],
    "Netherlands": ["cold", "modern", "urban", "luxury", "international"],
    "Ireland": ["cold", "historical", "nature", "budget", "local"],
    "Spain": ["warm", "modern", "urban", "luxury", "international"],
    "Sweden": ["cold", "modern", "nature", "budget", "local"],
    "Italy": ["warm", "historical", "urban", "luxury", "local"],
    "Latvia": ["cold", "historical", "nature", "budget", "local"],
    "Lithuania": ["cold", "historical", "nature", "budget", "local"],
    "Luxembourg": ["cold", "modern", "urban", "luxury", "international"],
    "Hungary": ["warm", "historical", "urban", "budget", "local"],
    "Malta": ["warm", "historical", "nature", "luxury", "local"],
    "Poland": ["cold", "historical", "urban", "budget", "local"],
    "Portugal": ["warm", "modern", "urban", "luxury", "local"],
    "Romania": ["cold", "historical", "nature", "budget", "local"],
    "Slovakia": ["cold", "historical", "nature", "budget", "local"],
    "Slovenia": ["cold", "historical", "nature", "budget", "local"],
    "Greece": ["warm", "historical", "urban", "luxury", "local"]
};

let userPreferences = [];
let currentQuestion = -1;
const chatContent = document.getElementById("chatContent");
const chatBox = document.getElementById("chatBox");

function toggleChat() {
    chatBox.style.display = (chatBox.style.display === "flex") ? "none" : "flex";
    if (chatBox.style.display === "flex") {
        startChat();
    }
}

function startChat() {
    chatContent.innerHTML = "";
    currentQuestion = -1;
    userPreferences = [];

    const firstMessage = document.createElement("div");
    firstMessage.classList.add("chat-message", "intro-message");
    firstMessage.innerText = "Are you unsure about which country to visit?";
    chatContent.appendChild(firstMessage);

    setTimeout(() => {
        firstMessage.classList.add("fade-up");
        setTimeout(() => {
            firstMessage.remove();
            showQuestion();
        }, 1500);
    }, 2000);
}

function showQuestion() {
    if (currentQuestion < questions.length - 1) {
        currentQuestion++;

        chatContent.innerHTML = ""; // Önceki içeriği temizle

        const questionObj = questions[currentQuestion];

        const messageDiv = document.createElement("div");
        messageDiv.classList.add("chat-message", "fade-in");
        messageDiv.innerText = questionObj.text;
        chatContent.appendChild(messageDiv);

        const buttonsDiv = document.createElement("div");
        buttonsDiv.classList.add("chat-buttons");

        Object.keys(questionObj.options).forEach(option => {
            const button = document.createElement("button");
            button.innerText = option;
            button.onclick = () => handleAnswer(questionObj.options[option]);
            buttonsDiv.appendChild(button);
        });

        chatContent.appendChild(buttonsDiv);

        adjustChatHeight();
    } else {
        showCountryRecommendation();
    }
}

function handleAnswer(answer) {
    userPreferences.push(answer);

    setTimeout(() => {
        showQuestion();
    }, 500);
}

// En uygun ülkeyi bul ve göster
function showCountryRecommendation() {
    chatContent.innerHTML = ""; // Önceki içeriği temizle

    let bestMatch = "";
    let maxMatches = 0;

    // Kullanıcının tercihlerine en çok uyan ülkeyi bul
    for (const country in countryPreferences) {
        let matches = countryPreferences[country].filter(pref => userPreferences.includes(pref)).length;

        if (matches > maxMatches) {
            maxMatches = matches;
            bestMatch = country;
        }
    }

    const resultMessage = document.createElement("div");
    resultMessage.classList.add("chat-message", "fade-in");
    resultMessage.innerText = `Based on your preferences, we recommend: ${bestMatch}! 🌍`;
    chatContent.appendChild(resultMessage);
}

function adjustChatHeight() {
    setTimeout(() => {
        chatBox.style.maxHeight = chatContent.scrollHeight + "px";
    }, 300);
}
