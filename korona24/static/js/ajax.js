 
function getQueryStringValue(key) {
    return decodeURIComponent(window.location.search.replace(new RegExp("^(?:.*[&\\?]" + encodeURIComponent(key).replace(/[\.\+\*]/g, "\\$&") + "(?:\\=([^&]*))?)?.*$", "i"), "$1"));
}


//Метод получения данных, передаём параметры в json, получаем в ответ данные.  
function GetResponse(arr,url) {
     
    $.ajax({
        url: url,
        method: "GET",
        data: JSON.stringify(arr),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        async: true,
        processData: false,
        contentType: false,
        success: function (data) {
            console.log(data);
            if (data.status == 200) {

                return data
            }
            console.error(data.status)
        },
		error: function (error) { // ошибка с сервера
            console.error(error);
            return null;
        }
    });
};

//Метод получения данных, передаём параметры url - адресс запроса, получаем в ответ данные.  
function GetAjaxData(url,data, callbackSucces) { 
     return $.ajax({ 
        url: url,
        method: "GET",
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        data: data,
        async: true, //формат данных 
        success: callbackSucces,
        error: function (response) { // данные не отправлены
            console.error(response);
            data = null;
        }
     }); 
} 

function popapSend(modal_id,form_id,url,modal_succes_id=null,hide=6500){ 
    
    if(!isValidPhone) return;
    sendAjaxForm(form_id,url,function(response){$("#" + form_id).reset()})  
    $("#" + modal_id).modal("hide")
    if(modal_succes_id != null){   
        console.log('send')
        $("#" + modal_succes_id).modal("show")
        setTimeout(function () {
            $("#" + modal_succes_id).modal("hide");
        }, hide);
    }
    return true;

}

function sendAjaxForm(form_id, url,callbackSucces = null) {
     
    $.ajax({
        url: url, //url страницы  
        type: "post", //метод отправки
        datatype: "html", //формат данных
        data: $("#" + form_id).serialize(),  // сеарилизуем объект
        success: function (response) { //данные отправлены успешно 
            if (response.status == 200) {
                if(callbackSucces)
                callbackSucces(response)
            }
        },
        error: function (response) { // данные не отправлены
            console.log(response);
        }
    });

}