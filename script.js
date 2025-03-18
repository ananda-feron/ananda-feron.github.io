// show and display sidebar func
function showSidebar() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.style.display = 'flex'; // Show the sidebar
}

function hideSidebar() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.style.display = 'none'; // Hide the sidebar
}

<script>
    let currentIndex = 0;
    const carouselItems = document.querySelectorAll('.carousel-item');
    const totalItems = carouselItems.length;

    // Function to show the next image
    function showNextImage() {
        // Remove 'levitate' class from the current item
        const currentItem = carouselItems[currentIndex];
        currentItem.classList.remove('levitate');

        // Move to the next item
        currentIndex = (currentIndex + 1) % totalItems; // Wrap around the index to the first item after the last
        const nextItem = carouselItems[currentIndex];
        nextItem.classList.add('levitate'); // Add 'levitate' class to the next image

        // Move the carousel container to the correct position
        const offset = -100 * currentIndex; // 100% width per image
        document.querySelector('.carousel-container').style.transform = `translateX(${offset}%)`;
    }

    // Start the carousel rotation
    setInterval(showNextImage, 5000); // Change image every 5 seconds
</script>
