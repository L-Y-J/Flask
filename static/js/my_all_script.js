/**
 * Created by yongjie on 2016/1/5 0005.
 */

var randomScalingFactor = function () {
    return Math.round(Math.random() * 100);
};

var startDate = function () {
    var local_date = $('#start-date').val();
    return local_date.split(/[\u4e00-\u9fa5]/, 3).join(':');
};

var endDate = function () {
    var local_date = $('#end-date').val();
    return local_date.split(/[\u4e00-\u9fa5]/, 3).join(':');
};

var baseGet = function (url, param, callBack) {
    $.ajax({
        type: 'GET',
        url: url,
        data: param,
        dataType: 'json',
        success: function (jsonData) {
            callBack(jsonData);
        }
    });
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

var drewCharts = function (canvas_id) {
    if (canvas_id === 'canvas' || canvas_id === undefined) {
        if (window.myLine !== undefined) {
            window.myLine.destroy();
        }
        var ctx = document.getElementById("canvas").getContext("2d");
        window.myLine = new Chart(ctx).Line(lineData, {
            responsive: true,
            multiTooltipTemplate: "<%= datasetLabel %> - <%= value %>"
        });
    }
    if (canvas_id === 'canvas3' || canvas_id === undefined) {
        if (window.myPie !== undefined) {
            window.myPie.destroy();
        }
        var ctx2 = document.getElementById("canvas3").getContext("2d");
        window.myPie = new Chart(ctx2).Pie(pieData, {
            responsive: true,
            multiTooltipTemplate: "<%= datasetLabel %> - <%= value %>"
        });
    }
    if (canvas_id === 'canvas4' || canvas_id === undefined) {
        if (window.myLine4 !== undefined) {
            window.myLine4.destroy();
        }
        var ctx3 = document.getElementById("canvas4").getContext("2d");
        window.myLine4 = new Chart(ctx3).Bar(lineData, {
            responsive: true,
            multiTooltipTemplate: "<%= datasetLabel %> - <%= value %>"
        });
    }
};

var queryData = function () {
    baseGet('/chartdata', {'startDate': startDate(), 'endDate': endDate()}, function (jsonData) {
        lineData.labels = jsonData.timeLine;
        drewCharts('canvas');
        drewCharts('canvas4');
    });
};

$(window).load(function () {
    $('.input-append.date').datepicker({
        todayBtn: "linked",
        language: "zh-CN",
        todayHighlight: true
    });

    drewCharts();
});

$(function () {
    $('#query-data').on('click', queryData);
});
