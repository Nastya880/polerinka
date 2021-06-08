$(function(){
    $("#like").click(function(){
        var likeButton = $("#like");
        var dislikeButton = $("#dislike");
        $.ajax({
            url: '/post/rating',
            data: {"type": 'like', "post": postId},
            type: 'post',
            success: function(result){
                likeButton.val(result.likes);
                dislikeButton.val(result.dislikes);
                alert(result.message);
            }
        });
    });
});
$(function(){
    $("#dislike").click(function(){
        var likeButton = $("#like");
        var dislikeButton = $("#dislike");
        $.ajax({
            url: '/post/rating',
            data: {"type": 'dislike', "post": postId},
            type: 'post',
            success: function(result){
                likeButton.val(result.likes);
                dislikeButton.val(result.dislikes);
                alert(result.message);
            }
        });
    });
});
setInterval(function(){
    var likeButton = $("#like");
    var dislikeButton = $("#dislike");
    $.ajax({
        url: '/post/rating',
        data: {"post": postId},
        type: 'get',
        success: function(result){
            likeButton.val(result.likes);
            dislikeButton.val(result.dislikes);
        }
    });
}, 1000);

