import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

def create_model(input_shape, num_classes):
    model = Sequential([
        # Convolutional layer with 32 filters, kernel size of 3x3, ReLU activation
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D((2, 2)),
        Dropout(0.25),  # Dropout layer for regularization

        # Second convolutional layer with 64 filters
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Dropout(0.25),

        # Flatten the output of the conv layers to feed into a dense layer
        Flatten(),

        # Dense layer with 128 units and ReLU activation
        Dense(128, activation='relu'),
        Dropout(0.5),

        # Output layer with softmax activation
        Dense(num_classes, activation='softmax')
    ])

    return model

input_shape = (spectrogram_height, spectrogram_width, 1)  # Update with your spectrogram dimensions
num_classes = 10  # Update with your number of classes

model = create_model(input_shape, num_classes)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


# Assuming you have your spectrogram data in `X_train`, `X_val`, `y_train`, and `y_val`
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=32)
