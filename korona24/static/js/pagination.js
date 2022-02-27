
let current_page = 1
let components_view = [] 

$(document).ready(function() {
    UpdatePage('pagination/',1)
});

function UpdateNumberPageView(page_max) { 
    console.log(1111111111)
    console.log(page_max)
    if(page_max <= 2)
    { 
        
        $("a[id=page_number_1]").hide() 
        $("a[id=page_number_2]").hide() 
        $("a[id=page_number_3]").hide()  
    }
    else
    {
        
        $("a[id=page_number_1]").show()
        $("a[id=page_number_2]").show()
        $("a[id=page_number_3]").show()
        $("a[id=page_number_1]").text(current_page-1)
        $("a[id=page_number_2]").text(current_page)
        $("a[id=page_number_3]").text(current_page+1) 
    }
}

function BackPage(url) {
    if(current_page > 0)
    { 
        UpdatePage(url,current_page - 1)
    }
}
function NextPage(url) { 
    UpdatePage(url,current_page + 1)
}
function UpdatePage(url,new_page){ 
    console.log("page",new_page)
    current_page = new_page
    data = {'page_num': new_page}
    AjaxJsonRequest(url,data,function (response) { // получение данных новой страницы
          console.log(response)
          UpdateComponents(response.articles)
          UpdateNumberPageView(response.page_max)
    },method='GET');
}
function UpdateComponents(components)
{ 
    
    RemoveOldComponentsView()
    components.forEach(element => { 
        console.log(element)
        AddNewComponentView(element) 
    });
    if(current_page == 1) 
        $("button[id=back_page]").hide()
    else 
        $("button[id=back_page]").show()

    $("#article_view").css("display", "none");
}
function AddNewComponentView(element)
{
    var msgCompanent = $("#article_view").clone(); 
    msgCompanent.appendTo(".blog__items");
    msgCompanent.show();
    msgCompanent.attr('id', 'article_' + element.id);
    msgCompanent.find(".blog__item-img").attr('href', element.url);
    msgCompanent.find("#img").attr('src', element.image_url)
    msgCompanent.find(".blog__item-img").attr('href', element.url);
    msgCompanent.find(".blog__item-title").attr('href', element.url); 
    msgCompanent.find(".blog__item-title").text(element.title); 
    msgCompanent.find(".blog__item-desc").text(element.description);  
    components_view.push(msgCompanent)
}
function RemoveOldComponentsView() {
    console.log(components_view)
    components_view.forEach(element => { 
        element.remove()
    });
}
function AjaxJsonRequest(url, data, callbackSucces,method = "POST") { 
    return $.ajax({ 
       url: url,
       method: method,
       contentType: 'application/json; charset=utf-8',
       dataType: 'json',
       data: data, //формат данных 
       async: true,
       success: callbackSucces,
       error: function (response) { // данные не отправлены
           console.error('error ajax request  ' + url); 
       }
    }); 
}
