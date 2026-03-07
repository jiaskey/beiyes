from core.pipeline import TrendPipeline


if __name__ == "__main__":
    pipeline = TrendPipeline(config_path="config/sources.yaml")
    pipeline.run()
