let multiply = document.getElementById("*");
let plus = document.getElementById("+");
let minus = document.getElementById("-");
let devision = document.getElementById("/");
let clear = document.getElementById("c");
let display = document.getElementById("display");
let equals = document.getElementById("=");
let ops = [];

window.onload = function () {
  try {
    display.value = localStorage.getItem("equation");
  } catch (e) {
    display.value = "";
  }
};

let buttons = [];
for (let i = 0; i < 10; i++) {
  buttons.push(document.getElementById(i));
}
buttons.push(multiply, plus, minus, devision);

for (let i = 0; i < buttons.length; i++) {
  buttons[i].style = "font-size:30px";
  buttons[i].onclick = function () {
    show(buttons[i].value);
    ops.push(buttons[i]);
  };
}

clear.onclick = function () {
  display.value = "";
  localStorage.setItem("equation", "");
};

equals.onclick = function () {
  let str = display.value;
  try {
    if (display.value != "") {
      display.value = eval(str);
      localStorage.setItem("equation", display.value);
    } else {
      console.error("display is empty");
      localStorage.setItem("equation", "");
    }
  } catch (err) {
    alert(err.message);
    display.value = "";
  }
};

function show(arg) {
  let random = Math.floor(Math.random() * 100);
  display.value += arg;
  localStorage.setItem("equation", display.value);

  if (random == 22) {
    if (confirm("Would you like to know how the calculator was built?")) {
      chrome.tabs.create({ url: "http://127.0.0.1:5000" });
    }
  }
}
