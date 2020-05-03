// const best = document.querySelector(`.selected`);
// const recent = document.querySelector(`.unselected`);

const favorite = document.querySelectorAll(`.favorite`);
const heart = document.querySelectorAll(`.fa-heart`);
const scroll = document.querySelectorAll(".scroll");

// const SELECTED = `selected`;
// const UNSELECTED = `unselected`;

const promptSelected = `selected__prompt`;

let isHeartClicked = false;

// function handleBest(event) {
//   if (best.classList === SELECTED){
//     best.classList = UNSELECTED;
//   }
//   else{
//     NodeList.classList = SELECTED;
//   }
// }

// function handleMenuNew(event) {
//   if (newList.classList === SELECTED) {
//   } else {
//     newList.classList = SELECTED;
//     bestList.classList = UNSELECTED;
//   }
// }

function handleHeart(event) {
  event.toElement.classList.add(`color__yellow`);
  const heartCount = event.target.parentNode.children[1];
  if (isHeartClicked === false){
    heartCount.innerText = parseInt(heartCount.innerText) + 1;
    isHeartClicked = true;
  }
  else{
    if (parseInt(heartCount.innerText) <= 0){
      heartCount.innerText = 0;
    }
    else{
      heartCount.innerText = parseInt(heartCount.innerText) - 1;
      isHeartClicked = false;
      event.toElement.classList.remove('color__yellow');
    }
  }
}

function scrollAppear(event) {
  event.style.transition = "all 1s ease-in-out";
  event.classList.add("gone");
  window.addEventListener("scroll", () => {
    let elPos = event.getBoundingClientRect().top,
      pos = window.innerHeight / 0.9;

    if (elPos < pos) {
      event.classList.add("appear");
    } else {
      event.classList.remove("appear");
    }
  });
}

function init() {
  // best.addEventListener("click", handleBest);
  // recent.addEventListener("click", handleRecent);

  heart.forEach(function(elem){
    elem.addEventListener("click", handleHeart)
  });

  scroll.forEach((item) => {
    scrollAppear(item);
  });

  window.scrollTo(1, 1);
}

init();
