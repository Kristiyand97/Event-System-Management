<script>
    document.addEventListener("DOMContentLoaded", function() {
        const form = document.querySelector("form");
        form.addEventListener("submit", function(event) {
            // Basic validation example
            const username = form.querySelector("#id_username").value;
            if (username.length < 3) {
                alert("Username must be at least 3 characters long.");
                event.preventDefault();
            }
        });
    });
</script>
