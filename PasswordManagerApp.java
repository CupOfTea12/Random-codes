import javafx.application.Application;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;

public class PasswordManagerApp extends Application {

    private final ObservableList<PasswordEntry> passwordEntries = FXCollections.observableArrayList();
    private TableView<PasswordEntry> tableView;
    private TextField nameField;
    private PasswordField passwordField;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Password Manager");
        BorderPane root = new BorderPane();

        // Create table view
        tableView = new TableView<>();
        tableView.setItems(passwordEntries);
        TableColumn<PasswordEntry, String> nameColumn = new TableColumn<>("Name");
        nameColumn.setCellValueFactory(cellData -> cellData.getValue().nameProperty());
        TableColumn<PasswordEntry, String> passwordColumn = new TableColumn<>("Password");
        passwordColumn.setCellValueFactory(cellData -> cellData.getValue().passwordProperty());

        tableView.getColumns().addAll(nameColumn, passwordColumn);

        // Create input fields
        nameField = new TextField();
        nameField.setPromptText("Name");
        passwordField = new PasswordField();
        passwordField.setPromptText("Password");

        // Create buttons
        Button addButton = new Button("Add Password");
        addButton.setOnAction(e -> addPassword());
        Button editButton = new Button("Edit Password");
        editButton.setOnAction(e -> editPassword());

        HBox inputBox = new HBox(10, nameField, passwordField, addButton, editButton);
        inputBox.setPadding(new Insets(10));
        inputBox.setSpacing(5);

        root.setCenter(tableView);
        root.setBottom(inputBox);

        primaryStage.setScene(new Scene(root, 600, 600));
        primaryStage.show();
    }

    private void addPassword() {
        String name = nameField.getText();
        String password = passwordField.getText();
        if (!name.isEmpty() && !password.isEmpty()) {
            passwordEntries.add(new PasswordEntry(name, password));
            nameField.clear();
            passwordField.clear();
        }
    }

    private void editPassword() {
        PasswordEntry selectedEntry = tableView.getSelectionModel().getSelectedItem();
        if (selectedEntry != null) {
            String newName = nameField.getText();
            String newPassword = passwordField.getText();
            if (!newName.isEmpty() && !newPassword.isEmpty()) {
                selectedEntry.setName(newName);
                selectedEntry.setPassword(newPassword);
                tableView.refresh();
                nameField.clear();
                passwordField.clear();
            }
        }
    }

    public static class PasswordEntry {
        private final StringProperty name = new SimpleStringProperty("");
        private final StringProperty password = new SimpleStringProperty("");

        public PasswordEntry(String name, String password) {
            setName(name);
            setPassword(password);
        }

        public String getName() {
            return name.get();
        }

        public void setName(String name) {
            this.name.set(name);
        }

        public String getPassword() {
            return password.get();
        }

        public void setPassword(String password) {
            this.password.set(password);
        }

        public StringProperty nameProperty() {
            return name;
        }

        public StringProperty passwordProperty() {
            return password;
        }
    }
}
