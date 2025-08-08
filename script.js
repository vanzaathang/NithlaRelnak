var timeBox = $(".time-box");
var currentDay = $("#currentDay");
var clearCal = $(".clearBtn");
var scheduleSec = $(".schedule-sec");

// Format Date and time using moment.js library
var currentDate = moment().format("dddd, MMMM Do");
var currentHour = moment().format("H");
// var currentDate = moment().format("MMM DD, YYYY [at] hh:mm:ss a");

// Declare arrray for all toDoLists
var toDoList = [];

// Set up the array of objects for toDolist
function initScheduler() {
  timeBox.each(function () {
    var currentTimeSec = $(this);
    var currentBoxTime = parseInt(currentTimeSec.attr("hour-sect"));

    // store related time and notes same with hour-sect
    var toDoObject = {
      hour: currentBoxTime,
      note: "",
    };
    toDoList.push(toDoObject);
  });

  localStorage.setItem("toDo", JSON.stringify(toDoList));
}

// Paint colors for past,current and future time section
function paintTimeBox() {
  timeBox.each(function () {
    var currentTimeSec = $(this);
    var currentBoxTime = parseInt(currentTimeSec.attr("hour-sect"));

    // paint colors depending on time
    if (currentBoxTime == currentHour) {
      currentTimeSec.addClass("present").removeClass("past future");
    } else if (currentBoxTime < currentHour) {
      currentTimeSec.addClass("past").removeClass("future present");
    } else if (currentBoxTime > currentHour) {
      currentTimeSec.addClass("future").removeClass("past present");
    }
  });
}

// save handler
function saveHandler() {
  var updateHour = $(this).parent().attr("hour-sect");
  var addItem = $(this).parent().children("textarea").val();

  for (var i = 0; i < toDoList.length; i++) {
    if (toDoList[i].hour == updateHour) {
      toDoList[i].note = addItem;
    }
  }
  localStorage.setItem("toDo", JSON.stringify(toDoList));
  renderSchedule();
}

// render function
function renderSchedule() {
  toDoList = localStorage.getItem("toDo");
  toDoList = JSON.parse(toDoList);

  for (var i = 0; i < toDoList.length; i++) {
    $("[hour-sect=" + toDoList[i].hour + "]")
      .children("textarea")
      .val(toDoList[i].note);
  }
}

// Clear calendar function
function clearCalendar() {
  localStorage.clear("toDo");
  saveHandler();
  renderSchedule();
}

// load the document
$(document).ready(function () {
  // call paintTimeBox function
  paintTimeBox();
  // if local storage is empty
  if (!localStorage.getItem("toDo")) {
    // call initScheduler function
    initScheduler();
  }
  //display current date
  currentDay.text(currentDate);

  // render schedule from local storage
  renderSchedule();
  // When save button is click
  scheduleSec.on("click", "button", saveHandler);
  clearCal.on("click", "button", clearCalendar);
});
