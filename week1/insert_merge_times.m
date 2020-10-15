figure
subplot(2, 2, 1)
semilogx(n_insert, time_insert, 'ro')
hold on
semilogx(n_merge, time_merge, 'bx')
hold on 
semilogx(n_stooge, time_stooge, 'go')
title('Insert, Merge, & Stooge Sort Times Comparison')
