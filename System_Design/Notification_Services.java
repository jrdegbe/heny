import java.util.*;

// User class represents a Heny user
class User {
    private String userId;
    private String name;
    private String phoneNumber;
    // other user attributes

    public User(String userId, String name, String phoneNumber) {
        this.userId = userId;
        this.name = name;
        this.phoneNumber = phoneNumber;
        // initialize other attributes
    }

    // Getters and setters for attributes
    // ...
}

// NotificationService class handles sending notifications to users
class NotificationService {
    private List<User> users;

    public NotificationService() {
        this.users = new ArrayList<>();
    }

    public void addUser(User user) {
        users.add(user);
    }

    public void sendNotification(String message) {
        for (User user : users) {
            sendSMS(user.getPhoneNumber(), message);
        }
    }

    private void sendSMS(String phoneNumber, String message) {
        // Logic to send SMS notification to the provided phone number
        // ...
    }
}

// Usage Example
public class Main {
    public static void main(String[] args) {
        NotificationService notificationService = new NotificationService();

        User user1 = new User("1", "Alice", "1234567890");
        User user2 = new User("2", "Bob", "9876543210");
        User user3 = new User("3", "Charlie", "5555555555");

        notificationService.addUser(user1);
        notificationService.addUser(user2);
        notificationService.addUser(user3);

        String message = "You have a new Recommender on Heny!";
        notificationService.sendNotification(message);
    }
}}
