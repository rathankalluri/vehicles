$(document).ready(function(){
    $("[data-toggle=tooltip]").tooltip();
    $(".btn[data-target='#edit']").click(function() {
        var data = [];
        data[0] = $(this).closest('tr').attr('id')
        var trvar = '#' + data[0];
        //console.log(trvar);
        i = 1;
        $(trvar).find('td').each(function(){
            data[i++] = $(this).text()
        });
        $('#a_auto_id').val(data[1])
        $('#a_auto_man').val(data[2])
        $('#a_year').val(data[3])
        $('#a_active').val(data[4])
        $('#a_dealer_id').val(data[5])

        console.log(data)

        //Show modal



        //On modal click Update
		//Update the table row AJAX
		/*$.ajax({
			type: 'POST',
			url: "update_new/",
			data: {
				'id': data[0],
				'auto_id': data[1],
				'auto_man': data[2],
				'year':data[3],
				'active': data[4],
				'dealer_id': data[5],
				'csrfmiddlewaretoken': '{{ csrf_token }}',
			},
			success: function(msg){
				console.log(msg)
				location.reload();
			}
		});
		*/
		//Update the table end


    //}});
    });
});