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
  year + "년 " + month + "월 " + date + "일 " + getTodayLabel(day) + "요일";

  //저장, 메인페이지에 넘겨주기
function saveDiary() {
  const currentDate  =
    year + "년 " + month + "월 " + date + "일 " + getTodayLabel(day) + "요일";
  const text = document.getElementById("content").value;
  
  localStorage.setItem('saveDate', currentDate);
  localStorage.setItem('saveText', text);

  window.location.href = "main.html";
}
