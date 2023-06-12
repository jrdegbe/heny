// User Class
class User {
    private String userId;
    private String name;
    private String bio;
    // other user attributes

    public User(String userId, String name, String bio) {
        this.userId = userId;
        this.name = name;
        this.bio = bio;
        // initialize other attributes
    }
}

// Like Class
class Like {
    private User liker;
    private User likee;
    private Date timestamp;

    public Like(User liker, User likee) {
        this.liker = liker;
        this.likee = likee;
        this.timestamp = new Date();
    }

    // Getters and setters
    // ...
}

// Match Class
class Match {
    private User user1;
    private User user2;
    private Date timestamp;

    public Match(User user1, User user2) {
        this.user1 = user1;
        this.user2 = user2;
        this.timestamp = new Date();
    }

    // Getters and setters
    // ...
}

// HenyApp Class
class HenyApp {
    private List<User> users;
    private List<Like> likes;
    private List<Match> matches;

    public HenyApp() {
        users = new ArrayList<>();
        likes = new ArrayList<>();
        matches = new ArrayList<>();
    }

    public void addUser(User user) {
        users.add(user);
    }

    public void addLike(User liker, User likee) {
        Like like = new Like(liker, likee);
        likes.add(like);

        // Check if there's a match
        if (likes.stream().anyMatch(l -> l.getLiker().equals(likee) && l.getLikee().equals(liker))) {
            Match match = new Match(liker, likee);
            matches.add(match);
            // Handle matched user notification or other actions
        }
    }

    // Other methods for handling user interactions, such as messaging, searching, etc.
    // ...
}

// Usage Example
public class Main {
    public static void main(String[] args) {
        HenyApp HenyApp = new HenyApp();

        User user1 = new User("1", "Alice", "I love hiking");
        User user2 = new User("2", "Bob", "I enjoy playing guitar");
        User user3 = new User("3", "Charlie", "I'm a foodie");

        HenyApp.addUser(user1);
        HenyApp.addUser(user2);
        HenyApp.addUser(user3);

        HenyApp.addLike(user1, user2);
        HenyApp.addLike(user2, user1);

        // Check for matches and perform further actions
        // ...
    }
}