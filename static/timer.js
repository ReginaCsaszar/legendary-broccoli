var taskPanelMini = $("#task-panel-mini"); 

var toggleDetails = function(show) {
  if (show) {
    taskPanelMini.show();
    $("#description").show();
    $("#goal").show();
    $("#spent").show();
  } else { 
    taskPanelMini.hide();
    $("#description").hide();
    $("#goal").hide();
    $("#spent").hide();
  }
};

toggleDetails(false);

$(document).ready(function(){
    
    var firstButton = $("#collapse1-control");
    firstButton.click(function() {
          if (firstButton.text() == "Pause") {
              firstButton.text("Start");
          } else {
              firstButton.text("Pause");
          };
          firstButton.toggleClass("btn-success")
    });

    var projectPanel = $("#project-panel");
    var leftPanel = $("#left-panel");
    var rightPanel = $("#right-panel");
    var statPanel = $("#stat-panel");
    var taskPanel = $("#task-panel");
    
    projectPanel.click(function() {
        leftPanel.removeClass("col-sm-4");
        leftPanel.addClass("col-sm-8");
        projectPanel.removeClass("project-hover");
        rightPanel.removeClass("col-sm-8");
        rightPanel.addClass("col-sm-4");
        taskPanel.hide();
        statPanel.hide();
        toggleDetails(true);
    });
    
    taskPanelMini.click(function() {
        leftPanel.removeClass("col-sm-8");
        leftPanel.addClass("col-sm-4");
        projectPanel.addClass("project-hover");
        rightPanel.removeClass("col-sm-4");
        rightPanel.addClass("col-sm-8");
        taskPanel.show();
        statPanel.show();
        toggleDetails(false);
    });
  

    google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours'],
          ['A successfull task',     100],
          ['My task',      50],
          ['Other task i see',  39],
          ['Other done task i see', 100],
          ['Another unassigned task',    0]
        ]);

        var options = {
          title: '',
          legend: 'none',
          slices: [{color: '#2d902d'}, {color: '#3cb8cc'}, {color: '#1b4ead'}, {color: '#3165c5'}, {}],
          chartArea: {top:30, width:'100%', height:'100%'}
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
});