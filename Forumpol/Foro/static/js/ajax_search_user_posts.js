urlMap = {"detalle_anuncio":'{% url foro:detalle_anuncio %}'}

function isEmpty(obj) {
    for(var key in obj) {
        if(obj.hasOwnProperty(key))
            return false;
    }
    return true;
}

$(document).ready(function(){
	$("#form-search").submit(function(e){
		e.preventDefault();
		$(".post-item").remove();
		$.ajax({
			url: $(this).attr('action'),
			type: $(this).attr('method'),
			data: $(this).serialize(),
			success: function(json){
				$table= $('ul.list-group');
				json["datos"].forEach(function(data){
					var $row= $('<li class="list-group-item post-item"></li>')
					var $a_content= $('<a href="">'+ data.content+'</a>')
					$a_content.attr("href", json["posts_url"]+data.id);
					var $span_owner= $('<span class="post-info pull-right user">'+ data.owner + '</span>')
					var $span_date= $('<span class="post-info pull-right fecha">' + data.date + '</span>')
					var $span_category= $('<span class="post-info pull-right user">' + data.category + '</span>')
					$row.append($a_content);
					$row.append($span_owner);
					$row.append($span_date);
					$row.append($span_category);
					$table.append($row);

				});
			}
		});
	});
});