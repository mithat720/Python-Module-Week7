def read_excel_from_drive(file_id):
    from auth import auth
    import io
    import pandas as pd
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaIoBaseDownload

    creds = auth()
    service = build("drive", "v3", credentials=creds)

    request = service.files().export_media(
        fileId=file_id,
        mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()

    fh.seek(0)
    df = pd.read_excel(fh)
    return df
