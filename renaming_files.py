from pathlib import Path

p = Path("c:/", "Users", "Eben Ofori-Mensah", "Downloads")
dest_dir = Path("C:\\Users\\Eben Ofori-Mensah\\Desktop\\Workstation\\Thesis Workspace\\Documentation\\Publishing\\Models\\CV results")
best_models_dir = dest_dir / "best_modesl"
final_models_dir = dest_dir / "final_models"
models_performance_dir = dest_dir / "model_performance"
resnet18_fold_files = p.glob("resnet18_fold_*.pth")

for file in resnet18_fold_files:
    new_name = file.name.replace("resnet18", "efficientnetB0")
    if "best" in file.name:
        file.rename(best_models_dir / new_name)
    elif "final" in file.name:
        file.rename(final_models_dir / new_name)
    elif "performance" in file.name:
        file.rename(models_performance_dir / new_name)
    else:
        print(f"File {file.name} does not match any expected patterns.")
        continue