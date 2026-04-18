<img width="1280" height="720" alt="2026-04-1822-36-44-ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/885eda3e-56b5-4cd0-bfec-ef4b6dd2ba5c" /># Sequential vs Parallel Algorithms: The King of Iron Fist Tournament

## Project Overview
This project explores the performance differences between sequential and parallel algorithms through the lens of a fighting game tournament bracket. We simulated entrant pools of varying sizes—from a 1,000-entrant Local Dojo to a 1,000,000-entrant Global EVO bracket—using generated Tekken Prowess scores as our dataset.

Our core objectives were to:
1. Seed the tournament brackets (Sorting) using both sequential and parallel Merge Sort architectures.
2. Locate a specific competitor's placement within the brackets (Searching) using sequential and parallel Linear Search implementations.

Performance Analysis & General Observations
Across our testing, we observed a clear threshold where the benefits of parallelization overtook its inherent overhead.

Small Datasets (1,000 elements): The sequential algorithms consistently outperformed the parallel implementations. The cost of instantiating multiprocessing.Process workers and establishing Inter-Process Communication (IPC) queues took longer than simply executing a single-threaded merge sort or linear search.

Large Datasets (1,000,000 elements): Parallel execution showed distinct advantages. By dividing the massive Global EVO bracket into four discrete blocks, our parallel algorithms were able to leverage multi-core processing, significantly cutting down execution time despite the final overhead of merging the sub-arrays.

Individual Reflections
Nash Andrew Bondoc (nathanjargon)
My biggest takeaway from leading this project was seeing that parallel processing isn't a magic fix for everything. The overhead of creating processes actually slowed down our small 1,000-element tests. Parallelism only became the better choice when we hit the massive 1,000,000-element dataset, where the sheer amount of computation finally outweighed the initial setup and synchronization time.

Lorenz Lacanaria (Dreuid)
Running the tests on my Acer Nitro V15, I realized that my 16GB of RAM wasn't the bottleneck—it was the CPU overhead required to manage the multiprocessing queues. The Tekken Prowess theme made the concept of "chunking" easy to visualize. The hardest part of the implementation was writing the synchronization logic to perfectly stitch those concurrent regional pools back into one global list without losing data or ruining the final search indexes.

Kyle Martin Sarmiento (slimetamer1)
Seeing the execution times side-by-side made the difference obvious. For the small 1,000-entrant bracket, the normal sequential sort was faster because it didn't have to waste time spawning multiple processes. But when we jumped to the 1,000,000-entrant EVO bracket, the parallel approach crushed it for sorting (1.38s vs 3.02s). Interestingly, parallelism wasn't universally better. For the Linear Search, sequential was always faster, even at 1 million elements, because searching an array is so computationally cheap that the overhead of process creation always slowed it down.

James Henry Emorricha (j4mesh3nry)
The toughest part of the code was figuring out how to pass data between isolated processes using a multiprocessing.Queue. We actually caught a fascinating bug during our EVO Global search test. The sequential search found our target at index 547241, while the parallel search found it at 1000000. This happened because a duplicate score was naturally generated in the middle of the dataset; sequential exited early upon finding it, while our parallel workers concurrently found both and the main process ended up logging the final appended target. It proved how much stricter state management needs to be in concurrent programming.

## How to Run the Evaluation
Ensure all modules (`dataset.py`, `sorting_sequential.py`, `sorting_parallel.py`, `search_sequential.py`, `search_parallel.py`) are in the same directory.
Run the main orchestrator:
```bash
python main.py

