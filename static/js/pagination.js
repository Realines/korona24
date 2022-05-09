
let current_page = 1
let max_pages = -1;
let components_view = [] 

$(document).ready(function() {
    UpdatePage('pagination/', 1)
});

function UpdateNumberPageView() { 
    // Обновление интерфейса пагинации.
    if (max_pages > 1) {
        if (current_page > 1 && current_page < max_pages) {
            $("button[id=back_page]").show()
            $("button[id=next_page]").show()
        }
        else if (current_page == 1) {
            $("button[id=back_page]").hide()
            $("button[id=next_page]").show()
        }
        else if (current_page == max_pages) {
            $("button[id=back_page]").show()
            $("button[id=next_page]").hide()
        }
    }
    else {
        $("button[id=back_page]").hide()
        $("button[id=next_page]").hide()
    }
}

function BackPage(url) {
    if(current_page > 1)
    { 
        UpdatePage(url, current_page - 1)
    }
}
function NextPage(url) { 
    if (current_page < max_pages) {
        UpdatePage(url,current_page + 1)
    }
}
function UpdatePage(url,new_page){ 
    console.log("page",new_page)
    current_page = new_page
    data = {'page_num': new_page}
    AjaxJsonRequest(url,data,function (response) { // получение данных новой страницы
          max_pages = response.max_pages;
          UpdateComponents(response.articles)
    },method='GET');
    UpdateNumberPageView()
}

function UpdateComponents(components)
{ 
    RemoveOldComponentsView()
    components.forEach(element => { 
        console.log(element)
        AddNewComponentView(element) 
    });
}

function AddNewComponentView(element)
{
    let msgCompanent = $("<div class='blog__item'></div"); 
    msgCompanent.appendTo(".blog__items");
    msgCompanent.show();
    msgCompanent.prop('id', 'article_' + element.id);

    let a_img = $("<a class='blog__item-img'></a>");
    a_img.prop('href', element.url);
    msgCompanent.append(a_img);

    let img = $("<img id='img_" + element.id + "'>");
    img.prop('src', element.image_url);
    a_img.append(img);

    let a_title = $("<a class='blog__item-title'></a>");
    a_title.prop('href', element.url);
    msgCompanent.append(a_title);
    msgCompanent.find(".blog__item-title").text(element.title);

    let div_desc = $("<div class='blog__item-desc'></div>");
    div_desc.text(element.description);
    msgCompanent.append(div_desc);

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
       dataType: 'json', //формат данных 
       data: data,
       async: false,
       success: callbackSucces,
       error: function (response) { // данные не отправлены
           console.error('error ajax request  ' + url); 
       }
    }); 
}
