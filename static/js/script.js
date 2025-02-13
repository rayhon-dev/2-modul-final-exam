// Modal functions
        function openModal() {
            document.getElementById('addNewModal').classList.remove('hidden');
            document.body.style.overflow = 'hidden'; // Prevent scrolling when modal is open
        }

        function closeModal() {
            document.getElementById('addNewModal').classList.add('hidden');
            document.body.style.overflow = 'auto'; // Re-enable scrolling
        }

        // Close modal when clicking outside
        window.onclick = function(event) {
            const modal = document.getElementById('addNewModal');
            if (event.target === modal) {
                closeModal();
            }
        }

        // Close modal on escape key press
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                closeModal();
            }
        });
    </script>
    <script>
        // Static data for charts
        const enrollmentData = {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [
                {
                    label: '2023 Enrollments',
                    data: [650, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1234],
                    borderColor: '#2563eb',
                    backgroundColor: 'rgba(37, 99, 235, 0.1)',
                    fill: true,
                    tension: 0.4
                },
                {
                    label: '2022 Enrollments',
                    data: [500, 550, 600, 650, 700, 750, 800, 850, 900, 920, 950, 980],
                    borderColor: '#9333ea',
                    backgroundColor: 'rgba(147, 51, 234, 0.1)',
                    fill: true,
                    tension: 0.4
                }
            ]
        };

        const subjectData = {
            labels: ['Science', 'Mathematics', 'Languages', 'Arts', 'Physical Education', 'Social Studies'],
            datasets: [{
                data: [30, 25, 20, 10, 8, 7],
                backgroundColor: [
                    '#2563eb',
                    '#9333ea',
                    '#06b6d4',
                    '#10b981',
                    '#f59e0b',
                    '#ef4444'
                ]
            }]
        };

        // Initialize charts
        const enrollmentChart = new Chart(document.getElementById('enrollmentChart'), {
            type: 'line',
            data: enrollmentData,
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: {
                            drawBorder: false
                        }
                    },
                    x: {
                        grid: {
                            display: false
                        }
                    }
                }
            }
        });

        const subjectChart = new Chart(document.getElementById('subjectChart'), {
            type: 'doughnut',
            data: subjectData,
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'right'
                    }
                }
            }
        });