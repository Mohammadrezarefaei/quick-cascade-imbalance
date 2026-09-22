import matplotlib.pyplot as plt
import os

def generate_png_chart(output_dir='outputs', filename='imbalance_cascade_plot.png'):
    """
    رسم نمودار مقایسه نرخ شکار عدم تعادل شبکه و ذخیره به صورت PNG
    """
    os.makedirs(output_dir, exist_ok=True)
    
    horizons = ['Day-Ahead (D-1)', 'Intraday Auction (IDA2)', '15-Min Before Delivery']
    our_model_recall = [45, 58, 89]      # درصد شکار مدل ما
    hackathon_team = [0, 0, 62]          # بنچمارک تیم هکاتون 50Hertz
    
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6), dpi=300)
    
    plt.plot(horizons, our_model_recall, marker='o', linewidth=3, markersize=8, color='#00CC96', label='Our 30-Min Cascade Model')
    plt.plot(horizons, hackathon_team, marker='s', linewidth=2, markersize=8, linestyle='--', color='#EF553B', label='50Hertz Hackathon Team')
    
    plt.title('System Imbalance Deficit Capture Rate Across Time Horizons', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Forecast Horizon', fontsize=10, labelpad=10)
    plt.ylabel('Deficit Capture Rate (%)', fontsize=10, labelpad=10)
    
    plt.ylim(-5, 105)
    plt.grid(True, linestyle=':', alpha=0.4, color='gray')
    plt.legend(frameon=True, facecolor='#1e2021', edgecolor='none')
    
    output_path = os.path.join(output_dir, filename)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"📈 Evaluation chart successfully saved at '{output_path}'!")

if __name__ == "__main__":
    generate_png_chart()
