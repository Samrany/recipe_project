"use strict";

$(document).ready(function() {


// Add recipe to favorites from homepage
$('.like_btn').on('click', (evt) => {
	evt.preventDefault();

	let recipe_id = evt.currentTarget.name
	
	console.log(evt)
	// console.log(evt.currentTarget.name)
	// console.log(evt.currentTarget.innerHTML)
		
	$.post('/user_fave', {'recipe_id':recipe_id}, (response) =>{
		
		// if response at status = ok then:
		evt.currentTarget.innerHTML = "&#9829"
	});
});


// Unfavorite recipes from favorites page
$('.unlike_btn').on('click', (evt) => {
	evt.preventDefault();

	console.log(evt)
	let recipe_id = evt.currentTarget.name;

	$.post('/user_unfave', {'recipe_id':recipe_id}, (response) =>{
		evt.currentTarget.innerHTML = '&#9825'		
	});

});

// let unlike_btn = document.getElementbyClassName('unlike_btn');

// unlike_btn.addEventListener("click", (evt) => {
// 	evt.preventDefault();
// 	console.log(evt);
// });


// Filter recipes by ingredient on homepage
const filter_input = document.getElementById('ingredient_filter');
// const recipe_cards = document.querySelectorAll('.card');

filter_input&&filter_input.addEventListener("keyup", (evt) => {
	evt.preventDefault();
	if (evt.keyCode === 13) {
		filter_input.click();



		let recipe_cards = $('.card').get()
			let ingredient = filter_input.value;
			
			for (const recipe of recipe_cards){
				console.log(recipe);
				console.log(recipe.textContent);
				if (recipe.textContent.includes(ingredient)) {		
					$(recipe.parentNode).removeClass("hidden_class");
			    }

			    else {
			   	 	$(recipe).parent().addClass("hidden_class");
			    }
			
			}
	}
});

});