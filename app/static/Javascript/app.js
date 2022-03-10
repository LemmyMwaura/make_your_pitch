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
