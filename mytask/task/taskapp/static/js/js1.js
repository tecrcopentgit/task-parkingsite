function toggleAnswer(element) {
    const answer = element.nextElementSibling;
    const isVisible = answer.style.display === "block";
    
    
    document.querySelectorAll('.faq-answer').forEach(ans => ans.style.display = "none");
    answer.style.display = isVisible ? "none" : "block";
  }