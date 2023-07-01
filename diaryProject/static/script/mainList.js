//오늘 날짜 받아오기
let today = new Date();

let year = today.getFullYear();
let month = today.getMonth() + 1;
let date = today.getDate();
let day = today.getDay();

function getTodayLabel(num) {
  var week = new Array("일", "월", "화", "수", "목", "금", "토");
  var todayLabel = week[num];

  return todayLabel;
}

document.getElementById("date").innerHTML =
  year + "년 " + month + "월 " + date + "일 ";

//일기 작성 페이지로 이동
function goToInputPage() {
  window.location.href = "input.html";
}

//타일 탭으로 변경
function goToTilePage() {
  window.location.href = "main.html";
}

//받아온 값으로 새로운 화이트박스 생성
document.addEventListener("DOMContentLoaded", function () {
  const diaryDate = localStorage.getItem("saveDate");
  const diaryText = localStorage.getItem("saveText");

  if (diaryText && diaryDate) {
    createWhiteBox(diaryDate, diaryText);
  }
});

function createWhiteBox(var1, var2) {
  const whiteBoxArea = document.getElementById("whiteBox");

  const whiteBox = document.createElement("div");
  whiteBox.className = "whiteBox";
  const whiteBoxContent = document.createElement("div");
  whiteBoxContent.className = "whiteBoxContent";
  const boxDate = document.createElement("div");
  boxDate.className = "boxDate";
  boxDate.innerHTML = var1;
  const count = document.createElement("div");
  count.className = "count"; 
  count.innerText = "(" + 2 + ")";
  const line = document.createElement("hr");
  line.className = "line";


  whiteBoxContent.appendChild(boxDate);
  whiteBoxContent.appendChild(count);
  whiteBoxContent.appendChild(line);
  whiteBox.appendChild(whiteBoxContent);
  whiteBoxArea.appendChild(whiteBox);
 

  whiteBox.onclick = function () {
    window.location.href = "check.html";
  };
}

function goToLoginPage() {
  window.location.href = "login.html";
}
