const axios = require("axios");

async function generateText(prompt) {
  const apiKey = process.env.OPENAI_API_KEY;
  const model = "text-davinci-002";
  const completionsEndpoint = `https://api.openai.com/v1/engines/${model}/completions`;

  const headers = {
    "Content-Type": "application/json",
    Authorization: `Bearer ${apiKey}`,
  };
  const data = {
    prompt: `${prompt}\n\n context: \n`,
    max_tokens: 100,
    n: 1,
    stop: null,
    temperature: 0.5,
  };
  const response = await axios.post(completionsEndpoint, data, { headers });
  const message = response.data.choices[0].text;
  return message;
}

async function run() {
  while (true) {
    const prompt = await ask("You: ");
    const response = await generateText(prompt);
    console.log("AI: " + response);
  }
}

run();

function ask(question) {
  const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  return new Promise((resolve) =>
    readline.question(question, (answer) => {
      resolve(answer);
      readline.close();
    })
  );
}
