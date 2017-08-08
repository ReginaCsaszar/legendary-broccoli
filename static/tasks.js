$(document).ready(function(){
    $(".task-hover").first().addClass("task-border");
    $(".task-hover").first().removeClass("task-hover")
    var progressBars = $(".progress-bar")
    for (let i = 0; i < progressBars.length; i++) {
            
            let timeArr = progressBars[i].dataset.goal.split(/:/);
            let goalTime = timeArr[0] * 3600 + timeArr[1] * 60 + timeArr[2];
            timeArr = progressBars[i].dataset.spent.split(/:/);
            let spentTime = timeArr[0] * 3600 + timeArr[1] * 60 + timeArr[2];
            let progress = Math.round(spentTime / goalTime * 100);
            $(progressBars[i]).attr("style", "width:" + progress + "%");
    };
});