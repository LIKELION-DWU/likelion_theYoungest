//내용 받아오기
document.addEventListener("DOMContentLoaded", function () {
  const var1 = localStorage.getItem("saveDate");
  const var2 = localStorage.getItem("saveText");

  document.getElementById("date").innerHTML = var1;
  document.getElementById("content").innerHTML = var2;
});

//수정
function correctionContent() {
  const contentTextarea = document.getElementById("content");

  if (contentTextarea.getAttribute("readonly")) {
    contentTextarea.removeAttribute("readonly");

    localStorage.setItem("saveText", document.getElementById("content").value);
  } else {
    contentTextarea.setAttribute("readonly", "readonly");
  }
}
//삭제
function deleteContent() {
  localStorage.removeItem("saveDate");
  localStorage.removeItem("saveText");
  window.location.href = "main.html";
}
//댓글수
document.getElementById("count").innerText = "댓글(" + 2 + ")";

function goToLoginPage() {
  window.location.href = "login.html";
}
