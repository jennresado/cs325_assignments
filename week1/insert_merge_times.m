figure
subplot(2, 2, 1)
plot(n_insert, time_insert, 'ro')
polyfit(log(n_insert), log(time_insert), 1)
hold on
plot(n_merge, time_merge, 'bx')
title('Insert vs Merge Sort Time Comparison')
