document.addEventListener('click', (e) => {
    const isDropDownButton = e.target.matches('[data-dropdown-button]')
    if(!isDropDownButton && e.target.closest('[data-dropdown]') != null) return;

    let currentDropdown
    if (isDropDownButton){
        currentDropdown = e.target.closest('[data-dropdown]')
        currentDropdown.classList.toggle('active')
    }
    document.querySelectorAll('[data-dropdown].active').forEach( dropdown => {
        if(dropdown === currentDropdown) return;
        dropdown.classList.remove('active')
    })
})

function like(postId) {
  const likesCount = document.getElementById(`likes-count-${postId}`)
  const likesButton = document.getElementById(`like-button-${postId}`)

  fetch(`/posts/like-post/${postId}`, {method: "POST"})
    .then((res) => res.json())
    .then((data) => {
      console.log(data)
      likesCount.innerText = data["likes"]
    })
    .catch((e) => alert("couldn't like post"))
}

