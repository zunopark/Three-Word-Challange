const promptTitle = document.getElementsByClassName("prompt__title");
const promptSpell = document.getElementsByClassName("write__prompt");
const submit = document.querySelector(`.submit`);

const PROMPT_LS = `prompt`;
const promptSet = localStorage.getItem(PROMPT_LS);
let promptLength = promptTitle.length;
const promptSelected = `selected__prompt`;

function handleSubmit(event) {
  location.href = "index.html";
}

function init() {
  for (let i = 0; i < promptLength; i++) {
    promptTitle[i].addEventListener("click", handleClick);
  }
  submit.addEventListener("click", handleSubmit);
  promptSpell[0].innerHTML = promptSet[0];
  promptSpell[1].innerHTML = promptSet[1];
  promptSpell[2].innerHTML = promptSet[2];
}

init();
