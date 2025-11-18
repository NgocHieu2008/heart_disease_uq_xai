# src/config.py

# Cấu hình dữ liệu
# Lưu ý: Hãy đảm bảo bạn đã đổi tên file tải về thành 'diabetes.csv'
DATA_PATH = "data/diabetes.csv"
MODEL_SAVE_PATH = "output/models/diabetes_model.pth"

# Cấu hình huấn luyện
BATCH_SIZE = 64            # Tăng lên vì dữ liệu lớn hơn
LEARNING_RATE = 0.001      # Learning rate tiêu chuẩn
EPOCHS = 200               # Số vòng lặp (200 là đủ cho bộ này)
DROPOUT_RATE = 0.2         # Tỷ lệ tắt node để tạo độ bất định
MC_SAMPLES = 50            # Số lần lấy mẫu Monte Carlo
TEST_SIZE = 0.2            # Tỷ lệ tập test (20%)
RANDOM_SEED = 42           # Cố định seed để kết quả không đổi