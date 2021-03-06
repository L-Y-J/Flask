/**
 * Created by yongjie on 2016/1/5 0005.
 */

var randomScalingFactor = function () {
    return Math.round(Math.random() * 100);
};

var startDate = function () {
    var local_date = $('#start-date').val();
    return local_date.split(/[\u4e00-\u9fa5]/, 3).join('-');
};

var endDate = function () {
    var local_date = $('#end-date').val();
    return local_date.split(/[\u4e00-\u9fa5]/, 3).join('-');
};

var lineData = {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
        {
            label: "My First dataset",
            fillColor: 'rgba(' + Math.floor(Math.random() * 200) + ', ' + Math.floor(Math.random() * 200) + ', ' + Math.floor(Math.random() * 200) + ', 0.5)',
            strokeColor: 'rgba(' + Math.floor(Math.random() * 200) + 20 + ', ' + Math.floor(Math.random() * 200) + 20 + ', ' + Math.floor(Math.random() * 200) + 20 + ', 0.5)',
            pointColor: 'rgba(' + Math.floor(Math.random() * 200) + 40 + ', ' + Math.floor(Math.random() * 200) + 40 + ', ' + Math.floor(Math.random() * 200) + 40 + ', 0.5)',
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: 'rgba(' + Math.floor(Math.random() * 200) + 60 + ', ' + Math.floor(Math.random() * 200) + 60 + ', ' + Math.floor(Math.random() * 200) + 60 + ', 0.5)',
            data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
        },
        {
            label: "My First dataset",
            fillColor: 'rgba(' + Math.floor(Math.random() * 200) + ', ' + Math.floor(Math.random() * 200) + ', ' + Math.floor(Math.random() * 200) + ', 0.5)',
            strokeColor: 'rgba(' + Math.floor(Math.random() * 200) + 20 + ', ' + Math.floor(Math.random() * 200) + 20 + ', ' + Math.floor(Math.random() * 200) + 20 + ', 0.5)',
            pointColor: 'rgba(' + Math.floor(Math.random() * 200) + 40 + ', ' + Math.floor(Math.random() * 200) + 40 + ', ' + Math.floor(Math.random() * 200) + 40 + ', 0.5)',
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: 'rgba(' + Math.floor(Math.random() * 200) + 60 + ', ' + Math.floor(Math.random() * 200) + 60 + ', ' + Math.floor(Math.random() * 200) + 60 + ', 0.5)',
            data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
        }
    ]
};

var pieData = [
    {
        label: "My Second dataset",
        value: 30,
        color: 'rgba(' + Math.floor(Math.random() * 200) + ', ' + Math.floor(Math.random() * 200) + ', ' + Math.floor(Math.random() * 200) + ', 0.5)'
    },
    {
        label: "My Second dataset",
        value: 50,
        color: 'rgba(' + Math.floor(Math.random() * 200) + ', ' + Math.floor(Math.random() * 200) + ', ' + Math.floor(Math.random() * 200) + ', 0.5)'
    },
    {
        label: "My Second dataset",
        value: 100,
        color: 'rgba(' + Math.floor(Math.random() * 200) + ', ' + Math.floor(Math.random() * 200) + ', ' + Math.floor(Math.random() * 200) + ', 0.5)'
    }
];

var drewCharts = function (canvasSet) {
    if (canvasSet.ctx) {
        if (window.myLine !== undefined) {
            window.myLine.destroy();
        }
        window.myLine = new Chart(canvasSet.ctx).Line(lineData, {
            responsive: true,
            multiTooltipTemplate: "<%= datasetLabel %> - <%= value %>"
        });
    }
    if (canvasSet.ctx2) {
        if (window.myPie !== undefined) {
            window.myPie.destroy();
        }
        window.myPie = new Chart(canvasSet.ctx2).Pie(pieData, {
            responsive: true,
            multiTooltipTemplate: "<%= datasetLabel %> - <%= value %>"
        });
    }
    if (canvasSet.ctx3) {
        if (window.myChart !== undefined) {
            window.myChart.destroy();
        }
        window.myChart = new Chart(canvasSet.ctx3).Bar(lineData, {
            responsive: true,
            multiTooltipTemplate: "<%= datasetLabel %> - <%= value %>"
        });
    }
};

var btnQuery = function () {
    if ($('#table').attr('class')) {
        window.location.href = '/table?startDate=' + startDate() + '&endDate=' + endDate();
    }
    if ($('#chart').attr('class')) {
        $.ajax({
            type: 'GET',
            url: '/chartdata',
            data: {'startDate': startDate(), 'endDate': endDate()},
            dataType: 'json',
            success: function (jsonData) {
                lineData.labels = jsonData['timeLine'];
                drewCharts({
                    ctx: document.getElementById("canvas") && document.getElementById("canvas").getContext("2d"),
                    ctx3: document.getElementById("canvas3") && document.getElementById("canvas3").getContext("2d")
                });
            }
        });
    }
};

$(window).load(function () {
    $('.input-append.date').datepicker({
        todayBtn: "linked",
        language: "zh-CN",
        todayHighlight: true
    });

    drewCharts({
        ctx: document.getElementById("canvas") && document.getElementById("canvas").getContext("2d"),
        ctx2: document.getElementById("canvas2") && document.getElementById("canvas2").getContext("2d"),
        ctx3: document.getElementById("canvas3") && document.getElementById("canvas3").getContext("2d")
    });
});

$(function () {
    $('#query-data').on('click', btnQuery);
});
