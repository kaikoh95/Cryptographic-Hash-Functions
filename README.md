# Cryptographic-Hash-Functions

-as adapted from University of Canterbury COSC362 S2-18 course, Lab 5.

Uses and compares cryptographic hash functions (one way and collision free) to demonstrate which one is easier to brute force than the other.

The One-Way Property

The one way property is what make hash functions a "trap door function", which is that you cannot reconstruct the message from any given hash.

It is defined as:

For any given hash h, it is computationally infeasible to find a message x, where H(x) = h

Let's say I give you a hash: ca21dcddb09a61249ee41445efcdd8fd9d568abbf955e582960d691ec72726b3

Can you reconstruct the message I hashed? Probably not, since I used SHA256, but if you do, let me know. I'll give you a chocolate fish for your efforts, while I go after the Bitcoin protocol.

Now, without doing any clever attacks on SHA256, it would take years, centuries or even the age of the universe to brute force every single message possible, to find one that matches that above hash.

But what if we did not use SHA256, and instead use a custom flawed hash function, which is limited to 24 bits? How many tries would it take?

We have prepared a program called OneWayBreaker.py which will do exactly this. Go ahead and run it, and run it several times to get an average number of tries it takes to brute force a randomly generated message.
The Collision-Free Property

The collision-free property comes in two variants. They are sometimes called different things, and they are:

Preimage resistance / weak collision resistance

and

Second preimage resistance / strong collision resistance

Now, weak collision resistance is defined as:

For any message x, it is computationally infeasible to find another message y, such that y≠x, and the hashes match: H(y) = H(x)

Now, to demonstrate this, imagine you got a contract to sign for an internship. It says you will be paid $18 an hour. It hashes to 2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3

If the hash algorithm had weak collision resistance, you would be able to tweak the contract to say you will be paid $25 an hour, and then brute force adding some random bytes to the end of the file, such that the hash matches the original. Then you could simply submit that version of the contract and get paid more.

Strong collision resistance is slightly different. It is defined as:

It is computationally infeasible to find any pair of messages (x, y) such than the hashes match: H(x) = H(y)

This is where you can always find, in a reasonable amount of time, a collision for any two arbitrary messages. Any two messages at all. Very hard.

Again, we have prepared a program called CollisionFreeBreaker.py which implements a brute force algorithm for weak collision resistance. The program is incomplete, and you will need to finish it. Read along the pseudo code, and modify the program as necessary.

Now, we can find out which one is easier to break using brute force.
