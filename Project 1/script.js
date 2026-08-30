// ---------------------------------------------------
// Rule-based response engine.
// Every reply below is an explicit, hand-written rule.
// No external calls, no generated logic, no frameworks.
// ---------------------------------------------------

const landing = document.getElementById("landing");
const startBtn = document.getElementById("startBtn");
const chatBox = document.querySelector(".chat-box");
const chatMessages = document.getElementById("chatMessages");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");
const exitBtn = document.getElementById("exitBtn");

// Rules stored as a dictionary (key -> reply).
// The key is the exact phrase to match against the cleaned-up input.
// A reply can be a plain string or a function that returns a string
// (used for values that change, like the current time or date).
const rules = {
  "help": "You can try: hello, your name, what can you do, time, date, joke, thank you, bye.",

  "hi": "Hello there. How can I help you today?",
  "hello": "Hello there. How can I help you today?",
  "hey": "Hello there. How can I help you today?",

  "your name": "I am Jarvis AI, a simple rule-based chat program.",
  "what is your name": "I am Jarvis AI, a simple rule-based chat program.",
  "who are you": "I am Jarvis AI, a simple rule-based chat program.",

  "what can you do": "I respond to a fixed set of phrases such as hello, time, date, and joke.",

  "time": () => "The current time is " + new Date().toLocaleTimeString() + ".",
  "what is the time": () => "The current time is " + new Date().toLocaleTimeString() + ".",

  "date": () => "Today's date is " + new Date().toLocaleDateString() + ".",
  "what is the date": () => "Today's date is " + new Date().toLocaleDateString() + ".",

  "joke": "Why did the developer go broke? Because he used up all his cache.",

  "thank you": "You are welcome.",
  "thanks": "You are welcome.",

  "bye": "Goodbye. Click the X button anytime to close this window.",
  "goodbye": "Goodbye. Click the X button anytime to close this window.",
  "exit": "Goodbye. Click the X button anytime to close this window.",
  "quit": "Goodbye. Click the X button anytime to close this window.",

  "how are you": "I am functioning as expected, thank you for asking."
};

// Default reply when no rule matches.
const defaultReply = "I did not understand that. Type \"help\" to see supported phrases.";

// Clean up the message before checking it against the dictionary.
function sanitizeInput(rawText) {
  return rawText.trim().toLowerCase().replace(/\s+/g, " ");
}

function getResponse(rawText) {
  const text = sanitizeInput(rawText);

  if (Object.prototype.hasOwnProperty.call(rules, text)) {
    const reply = rules[text];
    return typeof reply === "function" ? reply() : reply;
  }
  return defaultReply;
}

function addMessage(text, sender) {
  const msg = document.createElement("div");
  msg.classList.add("message", sender === "user" ? "user-message" : "bot-message");
  msg.textContent = text;
  chatMessages.appendChild(msg);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

function handleSend() {
  const text = userInput.value;
  if (text.trim() === "") return;

  addMessage(text, "user");
  userInput.value = "";

  const response = getResponse(text);
  // Small delay so the reply feels like a separate turn, not instant.
  setTimeout(() => addMessage(response, "bot"), 300);
}

startBtn.addEventListener("click", () => {
  landing.classList.add("hidden");
  chatBox.classList.add("visible");
  userInput.focus();
});

sendBtn.addEventListener("click", handleSend);

userInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    handleSend();
  }
});

exitBtn.addEventListener("click", () => {
  chatBox.classList.remove("visible");
  landing.classList.remove("hidden");
});
