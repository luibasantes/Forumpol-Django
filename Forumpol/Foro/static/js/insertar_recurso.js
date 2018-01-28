var counter=1;
$('[name=tags]')
    .tagify()
    .on('add', function(e, tagName){
        console.log('added', tagName)
});

$('#add_btn').click(function(e) {
	e.preventDefault();
	counter+= 1;
	$input= $('<input type="file" class="form-control-file" name="file_'+counter+'" accept="image/*,video/*,.doc,.docx,.xml,.pdf,.py"><br>')
	$input.insertBefore($(this))
	//$(this).parent().append($input)
});