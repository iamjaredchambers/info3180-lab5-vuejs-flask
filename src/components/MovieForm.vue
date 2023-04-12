<template>
     <form id="movieForm" @submit.prevent="saveMovie">
        <div class="mb-3">
        <label for="title" class="form-label" id = "form-label">Movie Title</label>
        <input type="text" name="title" class="formcontrol"/>
        <label for="description" class="form-label"> Description</label>
        <input type="text" name="description" class="formcontrol"/>
        <label for="poster" class="form-label">Poster</label>
        <input type ="file" class="formcontrol" name = "poster" />
        <button type="submit">Upload</button>
      
        
        <!-- Holy Spirit come into this code, I dont wanna fail at life ooooo. It will not be displayed on the webpage. -->

</div>
</form>
</template>

<script setup>
import { ref, onMounted } from 'vue';
let csrf_token = ref("");
let flashMessage = ref("");
let displayFlash = ref(false);
let isSuccess = ref(false);
let alertSuccessClass = ref("alert-success");
let alertErrorClass = ref("alert-danger"); 



onMounted(() => {
  getCsrfToken();
});
       function saveMovie()
        {
            let movieForm = document.getElementById('movieForm');
            let form_data = new FormData(movieForm);
            fetch('/api/v1/movies', 
            {
                method: 'POST',
                body: form_data,
                headers: {
                    "X-CSRFToken": csrf_token.value,
                }
            }) 
            .then(function(response) 
            {
                return response.json();
            })
            .then(function(data) 
            {
                console.log(data);
                
                // display success message or redirect to another page
             })
            .catch(function(error) 
            {
                console.log(error);
                console.log("Houston we have a problem")

    // display error message to user
            });
        }




function getCsrfToken() {
  fetch("/api/v1/csrf-token")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      csrf_token.value = data.csrf_token;
    });
}



</script>