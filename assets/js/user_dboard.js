function createGraphWidget() {
    var ctx = document.getElementById('graph-widget').getContext('2d');
    var myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
          label: 'Dataset 1',
          data: [0, 10, 5, 2, 20, 30, 45],
          borderColor: 'rgb(255, 99, 132)',
          borderWidth: 2
        }, {
          label: 'Dataset 2',
          data: [10, 20, 15, 12, 30, 40, 55],
          borderColor: 'rgb(54, 162, 235)',
          borderWidth: 2
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  }

window.addEventListener('load', function() {
    createGraphWidget();
  });
