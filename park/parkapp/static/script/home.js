function toggleAnswer(element) {
    const answer = element.nextElementSibling;
    const isVisible = answer.style.display === "block";
    
    // Close all open answers
    document.querySelectorAll('.faq-answer').forEach(ans => ans.style.display = "none");
  
    // Toggle current one
    answer.style.display = isVisible ? "none" : "block";
  }