// give and fundraise button finders
const giveBtn = document.getElementById("give");
const fundraiseBtn = document.getElementById("fundraise");
//
function setupHover(button, hoverBgColor, hoverTextColor, hoverBorderColor, leaveBgColor, leaveTextColor, leaveBorderColor) {
    button.addEventListener('mouseenter', () => {
    button.style.backgroundColor = hoverBgColor;
    button.style.color = hoverTextColor;
    button.style.borderColor = hoverBorderColor;
    // button.style.gap = hoverContainer
});
    button.addEventListener('mouseleave', () => {
        button.style.backgroundColor = leaveBgColor;
        button.style.color = leaveTextColor;
        button.style.borderColor = leaveBorderColor
    })
}

setupHover(giveBtn, 'black', 'rgb(253, 207, 31)', 'rgb(255, 255, 255)', 'rgb(253, 207, 31)', 'black', 'rgb(255, 207, 31)');
setupHover(fundraiseBtn, 'rgb(253, 207, 31)', 'black', 'rgb(253, 207, 31)',  'white', 'grey', 'grey');

const navButtons = document.querySelectorAll('.btn');

navButtons.forEach(button => {
  // Find the boxes next to this button
  const boxes = button.parentElement.querySelector('.boxes');

  // Mouse enters → increase gap
  button.addEventListener('mouseenter', () => {
    boxes.style.gap = '10px';
    boxes.querySelectorAll('.box').forEach( box => {
        box.style.backgroundColor = 'rgb(253, 207, 31)'
    });
    button.style.color = "black";
  });

  // Mouse leaves → reset gap
  button.addEventListener('mouseleave', () => {
    boxes.style.gap = '3px';
    boxes.querySelectorAll('.box').forEach(box => {
        box.style.backgroundColor = "grey"
    });
    button.style.color = "grey";
  });
});


  function textAnimation(element) {
    const characters= element.textContent.split("");
    element.textContent = "";

    characters.forEach((char, i ) => {
      const span = document.createElement("span");
      span.textContent = char === " " ? "\u00A0" : char;
      span.style.display ="inline";
      span.style.color = "black";
      element.appendChild(span);

      setTimeout(() =>{
      span.style.color ="rgb(253, 207, 31)"; } 
    ,i*200)
    });
  }

  window.addEventListener("DOMContentLoaded", () => {
    const textElement = document.querySelector(".moto");
    if (textElement) {
      textAnimation(textElement);
    }
  })




