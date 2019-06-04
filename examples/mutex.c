#include <pthread.h> 





int main() {
    pthread_mutex_t a;
    pthread_mutex_init(&a, NULL);

    for(int i=0; i<1000000000; ++i) {
        pthread_mutex_lock(&a);
        pthread_mutex_unlock(&a);
    }

    pthread_mutex_destroy(&a);
}