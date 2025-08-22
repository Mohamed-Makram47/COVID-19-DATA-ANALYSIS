import pandas as pd

def styled(obj, caption="", dots=False):
    if isinstance(obj, pd.Series):
        obj = obj.to_frame().T  # Convert Series to one-row DataFrame

    # Handle dots view for large DataFrames
    if dots and isinstance(obj, pd.DataFrame) and len(obj) > 6:
        head = obj.head(3)
        tail = obj.tail(3)

        # Create a DataFrame with the same columns and '...' as a row
        ellipsis_row = pd.DataFrame([['...'] * obj.shape[1]], columns=obj.columns)
        ellipsis_row.index = ['...']  # Set a placeholder index

        # Concatenate with original indexes preserved
        obj = pd.concat([head, ellipsis_row, tail])

    return (
        obj.style
        .set_properties(**{'text-align': 'left'})
        .set_table_styles([
            {'selector': 'th', 'props': [('text-align', 'left')]},
            {'selector': '.row_heading', 'props': [('text-align', 'left')]}
        ])
        .set_caption(caption)
    )
