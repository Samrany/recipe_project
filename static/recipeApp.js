"use strict";


$('.recipe_card').on('click', (evt) => {
	evt.preventDefault();

	let recipe_id = evt.currentTarget.name
	
	// console.log(evt)
	// console.log(evt.currentTarget.name)
	// console.log(evt.currentTarget.innerHTML)
		
	$.post('/user_fave', {'recipe_id':recipe_id}, (response) =>{
		
		// if response at status = ok then:
		evt.currentTarget.innerHTML = "Liked!"
		// otherwise print "You've already liked this one"
	});
});



	

		// $('#name-field').val(),
// f"hi my name is {name}"
//  hi my name is {name} 
// `
// `  ^ part of URL instead of part of body /user_fave/1. get in URL. Post in body.

