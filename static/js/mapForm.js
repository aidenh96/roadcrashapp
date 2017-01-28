// MAPFORM.JS 
// Controls vaildation for the Map selector
// Code By: Aiden Hussein
// NOTE: I realise this code is probably inefficient, but it works

$(document).ready(function(){
    
    $("#yrSingleSelect").hide();
    $(".yrMultiSelect").hide();
    
    $("input[name=yearRange]:radio").change(function () {
        
        if ($("#yrSingle").is(":checked")) {
            $('#yrSingleSelect').slideDown();
            $('.yrSingleInput').removeAttr('disabled');
            $('.yrMultiSelect').slideUp();
            $('.yrMultiInput').attr('disabled', 'disabled');
        }
        else if ($("#yrMulti").is(":checked")) {
            $('#yrSingleSelect').slideUp();
            $('.yrSingleInput').attr('disabled', 'disabled');
            $('.yrMultiSelect').slideDown();
            $('.yrMultiInput').removeAttr('disabled');
        }
    });
    
    $("#mapReset").click(function () {
        $("#yrSingleSelect").slideUp();
        $(".yrMultiSelect").slideUp();
        $("#yrSingleSelect option").removeAttr("disabled");
        $(".yrMultiSelect option").removeAttr("disabled");
    });
    
    $(".in1").change(function(){
        $('.in2>option:eq(1)').removeAttr('disabled');
        $('.in2>option:eq(2)').removeAttr('disabled');
        $('.in2>option:eq(3)').removeAttr('disabled');
        $('.in2>option:eq(4)').removeAttr('disabled');
        $('.in2>option:eq(5)').removeAttr('disabled');
        
        var selectedVal1 = $('.in1').val();
        
        if (selectedVal1 === '2011'){
            $('.in2>option:eq(1)').attr('disabled', 'disabled');
        }else if (selectedVal1 === '2012'){
            $('.in2>option:eq(1)').attr('disabled', 'disabled');
            $('.in2>option:eq(2)').attr('disabled', 'disabled');
        }else if (selectedVal1 === '2013'){
            $('.in2>option:eq(1)').attr('disabled', 'disabled');
            $('.in2>option:eq(2)').attr('disabled', 'disabled');
            $('.in2>option:eq(3)').attr('disabled', 'disabled');
        }else if (selectedVal1 === '2014'){
            $('.in2>option:eq(1)').attr('disabled', 'disabled');
            $('.in2>option:eq(2)').attr('disabled', 'disabled');
            $('.in2>option:eq(3)').attr('disabled', 'disabled');
            $('.in2>option:eq(4)').attr('disabled', 'disabled');
        }
    });
    
    $(".in2").change(function(){
        $('.in1>option:eq(1)').removeAttr('disabled');
        $('.in1>option:eq(2)').removeAttr('disabled');
        $('.in1>option:eq(3)').removeAttr('disabled');
        $('.in1>option:eq(4)').removeAttr('disabled');
        $('.in1>option:eq(5)').removeAttr('disabled');
        
        var selectedVal2 = $('.in2').val();
        
        if (selectedVal2 === '2014'){
            $('.in1>option:eq(5)').attr('disabled', 'disabled');
        }else if (selectedVal2 === '2013'){
            $('.in1>option:eq(4)').attr('disabled', 'disabled');
            $('.in1>option:eq(5)').attr('disabled', 'disabled');
        }else if (selectedVal2 === '2012'){
            $('.in1>option:eq(3)').attr('disabled', 'disabled');
            $('.in1>option:eq(4)').attr('disabled', 'disabled');
            $('.in1>option:eq(5)').attr('disabled', 'disabled');
        }else if (selectedVal2 === '2011'){
            $('.in1>option:eq(2)').attr('disabled', 'disabled');
            $('.in1>option:eq(3)').attr('disabled', 'disabled');
            $('.in1>option:eq(4)').attr('disabled', 'disabled');
            $('.in1>option:eq(5)').attr('disabled', 'disabled');
        }
    });
    
});