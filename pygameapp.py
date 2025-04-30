import pygame
import numpy as np
import cv2
from keras.models import load_model
import matplotlib.pyplot as plt

# Khởi tạo pygame
pygame.init()

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Kích thước màn hình
WIDTH, HEIGHT = 640, 480
DRAW_AREA = 280
OFFSET = 30

# Tạo cửa sổ
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nhận diện chữ viết tay A-Z")

# Tạo bề mặt vẽ
drawing = False
last_pos = None
canvas = pygame.Surface((DRAW_AREA, DRAW_AREA))
canvas.fill(BLACK)

# Load mô hình đã huấn luyện
model = load_model('D:\chuẩn\model_hand.h5')

# Từ điển ánh xạ số sang chữ cái
word_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',
             11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',
             21:'V',22:'W',23:'X',24:'Y',25:'Z'}

# Font chữ
font = pygame.font.SysFont('Arial', 30)

def preprocess_image(surface):
    """Tiền xử lý ảnh từ surface để phù hợp với mô hình"""
    # Chuyển surface thành mảng numpy
    data = pygame.surfarray.array3d(surface)
    
    # Chuyển ảnh sang grayscale và resize về 28x28
    img = cv2.cvtColor(data, cv2.COLOR_RGB2GRAY)
    img = cv2.resize(img, (28, 28))
    
    # Đảo ngược màu (nền đen chữ trắng -> nền trắng chữ đen)
    img = cv2.bitwise_not(img)
    
    # Chuẩn hóa
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    img = np.expand_dims(img, axis=-1)
    
    return img

def predict_letter(img):
    """Dự đoán chữ cái từ ảnh đã tiền xử lý"""
    predictions = model.predict(img)
    predicted_class = np.argmax(predictions)
    confidence = np.max(predictions)
    return word_dict[predicted_class], confidence

def main():
    global drawing, last_pos
    
    running = True
    prediction = ""
    confidence = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Bắt đầu vẽ
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                last_pos = event.pos
            
            # Kết thúc vẽ
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                last_pos = None
                
                # Tiền xử lý và dự đoán
                img = preprocess_image(canvas)
                prediction, confidence = predict_letter(img)
            
            # Xóa canvas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    canvas.fill(BLACK)
                    prediction = ""
                    confidence = 0
        
        # Vẽ nếu đang giữ chuột
        if drawing:
            mouse_pos = pygame.mouse.get_pos()
            if last_pos:
                # Chỉ vẽ trong vùng canvas
                if (OFFSET <= last_pos[0] <= OFFSET+DRAW_AREA and 
                    OFFSET <= last_pos[1] <= OFFSET+DRAW_AREA and
                    OFFSET <= mouse_pos[0] <= OFFSET+DRAW_AREA and 
                    OFFSET <= mouse_pos[1] <= OFFSET+DRAW_AREA):
                    
                    # Vẽ trên canvas (điều chỉnh tọa độ)
                    pygame.draw.line(canvas, WHITE, 
                                    (last_pos[0]-OFFSET, last_pos[1]-OFFSET), 
                                    (mouse_pos[0]-OFFSET, mouse_pos[1]-OFFSET), 15)
            last_pos = mouse_pos
        
        # Vẽ giao diện
        screen.fill(WHITE)
        
        # Vẽ khung canvas
        pygame.draw.rect(screen, BLACK, (OFFSET-2, OFFSET-2, DRAW_AREA+4, DRAW_AREA+4), 2)
        
        # Hiển thị canvas
        screen.blit(canvas, (OFFSET, OFFSET))
        
        # Hiển thị hướng dẫn
        instructions = font.render("Vẽ chữ cái vào khung đen", True, BLACK)
        screen.blit(instructions, (WIDTH//2 - instructions.get_width()//2, 10))
        
        clear_text = font.render("Nhấn 'C' để xóa", True, BLACK)
        screen.blit(clear_text, (WIDTH//2 - clear_text.get_width()//2, 50))
        
        # Hiển thị kết quả dự đoán
        if prediction:
            pred_text = font.render(f"Dự đoán: {prediction}", True, RED)
            conf_text = font.render(f"Độ chính xác: {confidence*100:.2f}%", True, RED)
            
            screen.blit(pred_text, (WIDTH//2 - pred_text.get_width()//2, HEIGHT - 100))
            screen.blit(conf_text, (WIDTH//2 - conf_text.get_width()//2, HEIGHT - 60))
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
